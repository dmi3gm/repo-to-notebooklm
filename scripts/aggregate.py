import os
import shutil
import subprocess
import re

# Настройки
LIMIT_SIZE_MB = 8  # Порог разделения файла
OUT_DIR = "out_ntbklm"

def log(msg):
    print(f"--- [INFO] {msg}")

def get_md_files(repo_path):
    md_files = []
    for root, dirs, files in os.walk(repo_path):
        # Игнорируем папки на точку (.git, .github и т.д.)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_path)
                md_files.append((rel_path, full_path))
    
    # Сортировка: README всегда первый, остальные по алфавиту
    def sort_key(item):
        path = item[0].lower()
        if 'readme.md' in path:
            return (0, path)
        return (1, path)
    
    md_files.sort(key=sort_key)
    return md_files

def split_content(content, repo_name):
    lines = content.splitlines()
    total_lines = len(lines)
    # Примерный расчет количества частей на основе размера
    size_mb = len(content.encode('utf-8')) / (1024 * 1024)
    parts_count = int(size_mb // LIMIT_SIZE_MB) + 1
    
    if parts_count <= 1:
        return [content]

    # Ищем заголовки ## для красивого разреза
    candidates = [i for i, line in enumerate(lines) if re.match(r'^##\s', line)]
    if not candidates:
        candidates = [i for i, line in enumerate(lines) if re.match(r'^#\s', line)]

    chunks = []
    last_idx = 0
    for i in range(1, parts_count):
        target = (total_lines // parts_count) * i
        split_idx = min(candidates, key=lambda x: abs(x - target))
        chunks.append("\n".join(lines[last_idx:split_idx]))
        last_idx = split_idx
    chunks.append("\n".join(lines[last_idx:]))
    return chunks

def process_repo(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    tmp_path = f"tmp_{repo_name}"
    
    log(f"Клонирование {repo_url}...")
    subprocess.run(["git", "clone", "--depth", "1", repo_url, tmp_path], check=True)
    
    md_files = get_md_files(tmp_path)
    combined_content = []
    
    for rel_path, full_path in md_files:
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Добавляем мета-заголовок пути для NotebookLM
            combined_content.append(f"\n\n# SOURCE_FILE: {rel_path}\n---\n")
            combined_content.append(content)
    
    full_text = "".join(combined_content)
    chunks = split_content(full_text, repo_name)
    
    os.makedirs(OUT_DIR, exist_ok=True)
    for i, chunk in enumerate(chunks):
        suffix = f"_part_{i+1}" if len(chunks) > 1 else ""
        out_file = os.path.join(OUT_DIR, f"{repo_name}{suffix}.md")
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(chunk)
        log(f"Сохранен файл: {out_file}")

    shutil.rmtree(tmp_path)

if __name__ == "__main__":
    repos = os.getenv("REPOS", "").split()
    for r in repos:
        if r: process_repo(r)
