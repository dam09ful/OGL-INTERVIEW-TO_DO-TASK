from tkinter import CURRENT
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


# chrome_options = webdriver.ChromeOptions
chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")
driver = webdriver.Chrome(executable_path=binary_path, options=chromeoptions)

URL = 'https://mdn.github.io/todo-react-build/'

driver.get(URL)

list_heading = driver.find_element(By.ID, 'list-heading').text
current_task = int(list_heading.split(' ')[0])

# print(list_heading)
# print(current_task)

print("All tasks before addding new task: " + str(current_task))
tasks = ['test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10']
for task in tasks:
    driver.find_element(By.ID, 'new-todo-input').clear()
    driver.find_element(By.ID, 'new-todo-input').send_keys(task)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/button').click()

# sleep(2)

new_task = int(driver.find_element(By.ID, 'list-heading').text.split(' ')[0])

if new_task > current_task:
    print('New task added')


print(f"ALL TASK: {driver.find_element(By.ID, 'list-heading').text}")

## PRINT ACTIVE TASKS
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button[2]').click()
active_task = driver.find_element(By.ID, 'list-heading').text
# print("ACTIVE TASKS: " + active_task) # Line 42 and 43 are the same. Line 43 uses f-formatting.
print(f"ACTIVE: {active_task}")

# CLICK ON ACTIVE TASK TO MARK AS COMPLETED
clicked_task = driver.find_elements(By.CLASS_NAME, 'todo-label')

task_completed = ['test2', 'test', 'test9']
for elem in clicked_task:
    for task in task_completed:
        if elem.text == task:
            elem.click()
            print(f"TASK COMPLETED: {task}")
            break

print(f"REMAINING ACTIVE TASK: {driver.find_element(By.ID, 'list-heading').text}")

## PRINT COMPLETED TASKS
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button[3]').click()
completed_task = driver.find_element(By.ID, 'list-heading').text

print(f"COMPLETED: {completed_task}")

driver.close()


