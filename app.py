import os

#comandos

#voltar ao menu
def voltar_menu():
    input('Digite uma tecla para voltar ao menu principal')
    main()

#limpar tela
def limpar_tela():
    os.system('cls')


#visuais


#--------------------------------------------------------
#listas/dicionarios
restaurantes = [{'nome': 'Res1', 'categoria': 'Japones', 'ativo': False}, {'nome': 'Res2', 'categoria': 'Pizza', 'ativo': True}, 
                {'nome': 'Res3', 'categoria': 'Árabe', 'ativo': False}]


#--------------------------------------------------------
#cadastrar restaurante
def cadastrar_restaurante():
    limpar_tela()
    print('Cadastro de Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()


#status restaurante (ativando)
def status_restaurante():
    limpar_tela()
    print('Alterando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu()

#--------------------------------------------------------
#listar restaurante
def listar_restaurantes():
    limpar_tela()
    print('Lista de Restaurantes cadastrados\n')
    print(f'{'Nome do Restaurante'.ljust(10)} | {'Categoria'.ljust(10)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')
    voltar_menu()

#--------------------------------------------------------
#aplicações
def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Status restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção Inválida\n')
    voltar_menu()

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            status_restaurante()
        elif opcao_escolhida == 4:
            encerrar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def encerrar_app():
    limpar_tela()
    print('Encerrando o app\n')

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()