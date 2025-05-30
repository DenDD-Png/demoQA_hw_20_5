from selene import browser, have


def test_browser_conf():
    #Конфигурации для браузера
    browser.config.driver_name = 'firefox'
    browser.config.driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://todomvc.com/'
    # Конфиг для тайм аута одного или нескольких элементов
    browser.element().with_(timeout=browser.config.timeout * 2)


def test_toddmvc():
    browser.config.base_url = 'https://todomvc.com/'

    browser.open('/examples/react/dist/')
    browser.element('.new-todo').type('Bla-bla-bla').press_enter()
    browser.all('.new-todd li').should(have.exact_texts('Bla-bla-bla'))

def test_todo():
    browser.open('https://todomvc.com/examples/react/dist/')
    #Поиск одного элемента
    new_todo = browser.element('.new-todo')
    #
    new_todo.type('First task').press_enter()
    new_todo.type('Second task').press_enter()
    new_todo.type('Third task').press_enter()
    # Поиск всех элементов с определенным локатором
    todo_items = browser.all('.todo-list li')
    # Поиск колекции элементов
    todo_items.should(
        have.exact_texts('First task','Second task', 'Third task')
    )

    #each проверяет каждую запись на наличие слова task
    todo_items.should(have.text('task').each)

def test_find_coll():
    browser.open('https://todomvc.com/examples/react/dist/')
    #Поиск одного элемента
    new_todo = browser.element('.new-todo')
    #
    new_todo.type('First task').press_enter()
    new_todo.type('Second task').press_enter()
    new_todo.type('Third task').press_enter()

    todo_items = browser.all('.todo-list li')

    first_element = todo_items[0]
    first_element_v2 = todo_items.element(0)
    first_element_v3 = todo_items.element_by_its('labal', have.text('First task'))

    assert first_element().id == first_element_v2().id == first_element_v3().id
