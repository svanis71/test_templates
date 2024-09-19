from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("jinja_test"),
    autoescape=select_autoescape(), trim_blocks=True
)
template = env.get_template("mytemplate.html")
data = [('Apa', 2, 'OK'),
        ('banan', 4, 'NOK'),
        ('citron', 1, 'HOK'),
        ('dadel', 3, 'OK'),
        ('Ekollon', 0, 'NOK'),
        ]
content = template.render(title='Test app for jinja', mydata=data)
with open('index.html', mode='w') as f:
    f.write(content)

