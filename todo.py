# todo.py
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Загружает задачи из файла"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Сохраняет задачи в файл"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_tasks():
    """Показывает все задачи"""
    tasks = load_tasks()
    if not tasks:
        print("📭 Список задач пуст")
        return
    
    print("\n📋 Ваши задачи:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['title']}")

def add_task():
    """Добавляет новую задачу"""
    title = input("Введите задачу: ").strip()
    if not title:
        print("❌ Задача не может быть пустой")
        return
    
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Добавлено: '{title}'")

def complete_task():
    """Отмечает задачу выполненной"""
    tasks = load_tasks()
    if not tasks:
        print("❌ Нет задач для завершения")
        return
    
    show_tasks()
    try:
        num = int(input("\nНомер задачи для завершения: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            save_tasks(tasks)
            print("✅ Задача завершена!")
        else:
            print("❌ Неверный номер")
    except ValueError:
        print("❌ Введите число")

def main():
    """Главное меню"""
    while True:
        print("\n" + "="*30)
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Завершить задачу")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор")

if __name__ == "__main__":
    main()