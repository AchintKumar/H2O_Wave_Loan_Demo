from h2o_wave import main, app, Q, ui, pack, data

@app('/demo')
async def serve(q: Q):
    q.page['header'] = ui.header_card(
    box='1 1 8 1',
    title='Loan Status',
    subtitle='',
    icon='LookupEntities',
    items=[ui.toggle(name='theme', label='Toggle dark theme')])
    
    q.page['form'] = ui.form_card(box='1 2 4 10', items=[
        ui.text_xl(content='Details for Loan Prediction'),
        ui.textbox(name='name_box', label='Name'),
        ui.date_picker(name='birth_date_picker', label='Date of Birth'),
        ui.dropdown(name='marital_dropdown', label='Marital Status', choices=[
            ui.choice(name=x, label=x) for x in ['Single','Married','Divorced']
        ]),
        ui.dropdown(name='education_dropdown', label='Highest Education', choices=[
            ui.choice(name=x, label=x) for x in ['MBA','Masters','Bachelors','12th','10th']
        ]),
        ui.textbox(name='Credit_Limit_Text', label='Credit Limit'),
        ui.textbox(name='Latest_Bill_Text', label='Latest Credit Bill'),
        ui.textbox(name='Latest_Paid_Text', label='Latest Credit Paid'),
        ui.button(name='show_inputs', label='Check Loan Status', primary=True),
    ])

    q.page['plot'] = ui.plot_card(
    box='5 2 4 5',
    title='Loan Prediction',
    data=data('year value', 8, rows=[
        ('1991', 3),
        ('1992', 4),
        ('1993', 3.5),
        ('1994', 5),
        ('1995', 4.9),
        ('1996', 6),
        ('1997', 7),
        ('1998', 9),
        ('1999', 13),
    ]),
    plot=ui.plot([ui.mark(type='line', x_scale='time', x='=year', y='=value', y_min=0)]))

    q.page['example'] = ui.markdown_card(
    box='5 7 4 1',
    title='',
    content='Based on the predictions, your loan will be approved'
)
    await q.page.save()

#@on()
async def theme(q: Q):
    q.page['meta'].theme = 'h2o-dark'