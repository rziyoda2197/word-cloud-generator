import concurrent.futures
import time

def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def parallelize_cpu_bound_tasks(tasks, num_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(cpu_bound_task, task): task for task in tasks}
        results = []
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            try:
                result = future.result()
                results.append((task, result))
            except Exception as e:
                print(f"Task {task} raised an exception: {e}")
        return results

if __name__ == "__main__":
    num_tasks = 10
    num_workers = 4
    tasks = [1000000 for _ in range(num_tasks)]
    start_time = time.time()
    results = parallelize_cpu_bound_tasks(tasks, num_workers)
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
```

Kod CPU-bound task parallelizeri uchun mo'ljallangan. U quyidagilarini qiladi:

1. `cpu_bound_task` funktsiyasi CPU-bound taskni bajaradi. U `n` qiymatining karraliy sonlarining kvadratlarining yig'indisini qaytaradi.
2. `parallelize_cpu_bound_tasks` funktsiyasi quyidagilarini qiladi:
 * `num_workers` miqdorida ishchi threadlar yaratadi.
 * Har bir taskni `cpu_bound_task` funktsiyasiga yuboradi.
 * Har bir taskning natijasini yig'laydi va natijalarni qaytaradi.
3. `if __name__ == "__main__":` qismida, kod CPU-bound tasklar soni va ishchi threadlar sonini belgilaydi. Keyin u CPU-bound tasklar soni bo'yicha 10 ta task yaratadi va ularni parallelizatsiya qiladi. Natijalarni konsolga chiqaradi va bajarilgan vazifaning vaqtini hisoblaydi.
