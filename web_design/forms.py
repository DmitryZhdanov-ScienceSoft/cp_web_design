from django import forms


class WebsiteBriefForm(forms.Form):
    company = forms.CharField(label='Название компании/проекта', max_length=100)
    contact = forms.CharField(label='Контактное лицо', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)
    email = forms.EmailField(label='Email')

    main_goal = forms.CharField(label='Основная цель создания сайта', widget=forms.Textarea)
    tasks = forms.CharField(label='Конкретные задачи сайта', widget=forms.Textarea)
    expected_results = forms.CharField(label='Ожидаемые результаты от запуска сайта', widget=forms.Textarea)

    target_audience = forms.CharField(label='Опишите вашу целевую аудиторию', widget=forms.Textarea)
    age = forms.CharField(label='Возраст', required=False)
    gender = forms.CharField(label='Пол', required=False)
    location = forms.CharField(label='Местоположение', required=False)
    interests = forms.CharField(label='Интересы', required=False)

    sections = forms.CharField(label='Необходимые разделы сайта', widget=forms.Textarea)
    interactive = forms.MultipleChoiceField(
        label='Требуемые интерактивные элементы',
        choices=[
            ('feedback-form', 'Форма обратной связи'),
            ('online-chat', 'Онлайн-чат'),
            ('calculator', 'Калькулятор'),
            ('other', 'Другое'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    other_interactive = forms.CharField(label='Другое (интерактивные элементы)', required=False)

    adaptive = forms.MultipleChoiceField(
        label='Требования к адаптивности',
        choices=[
            ('desktop', 'Десктоп версия'),
            ('mobile', 'Мобильная версия'),
            ('tablet', 'Планшетная версия'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    design_style = forms.CharField(label='Предпочтения по стилю дизайна', widget=forms.Textarea, required=False)
    color_scheme = forms.CharField(label='Цветовая гамма', required=False)
    example_sites = forms.CharField(label='Примеры сайтов, которые нравятся', widget=forms.Textarea, required=False)
    brand = forms.ChoiceField(
        label='Наличие готового фирменного стиля или логотипа',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        widget=forms.RadioSelect,
        required=False
    )

    content_provider = forms.ChoiceField(
        label='Кто будет предоставлять контент для сайта?',
        choices=[('client', 'Заказчик'), ('executor', 'Исполнитель'), ('both', 'Совместно')],
        widget=forms.RadioSelect,
        required=False
    )
    copywriting = forms.ChoiceField(
        label='Потребность в копирайтинге',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        widget=forms.RadioSelect,
        required=False
    )
    visual_content = forms.ChoiceField(
        label='Потребность в создании визуального контента',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        widget=forms.RadioSelect,
        required=False
    )

    hosting = forms.CharField(label='Требования к хостингу', widget=forms.Textarea, required=False)
    integration = forms.CharField(label='Необходимость интеграции с внешними сервисами', widget=forms.Textarea,
        required=False)

    seo = forms.CharField(label='Требования к SEO-оптимизации', widget=forms.Textarea, required=False)
    promotion = forms.CharField(label='Планы по продвижению сайта', widget=forms.Textarea, required=False)

    deadline = forms.CharField(label='Желаемые сроки реализации проекта', required=False)
    budget = forms.CharField(label='Бюджет на разработку сайта', required=False)

    additional_info = forms.CharField(label='Любые другие пожелания или требования', widget=forms.Textarea,
        required=False)