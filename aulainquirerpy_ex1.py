from InquirerPy import inquirer
nome = inquirer.text('Qual é o seu nome?').execute()
cor = inquirer.select('Qual é a sua cor favorita?',
                      choices=['azul','verde','vermelho']).execute()