import math

def calculadora_faltas_qacademico():
    while True:
        print("\n" + "="*60)
        print("--- Menu: Calculadora de Faltas (Padrão Q-Acadêmico) ---")
        print("1. Calcular limite e status da disciplina")
        print("0. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            print("Encerrando a calculadora...")
            break
            
        elif opcao == '1':
            try:
                disciplina = input("\nNome da Disciplina (ex: Lógica, Design Digital): ")
                
                # Pegando os dados baseados na estrutura do portal
                aulas_previstas = int(input("Número de aulas previsto (ex: 80): "))
                if aulas_previstas <= 0:
                    print("O número de aulas precisa ser maior que zero.")
                    continue
                    
                aulas_ministradas = int(input("Aulas ministradas até agora: "))
                
                # Novo menu para escolher como informar as faltas
                print("\nComo você quer informar as suas faltas atuais?")
                print("1. Por aulas avulsas (ex: 3 faltas no portal)")
                print("2. Por dias de falta (1 dia = 3 aulas)")
                tipo_falta = input("Escolha 1 ou 2: ")
                
                if tipo_falta == '2':
                    dias_falta = int(input("Quantos DIAS completos você já faltou? "))
                    faltas_atuais = dias_falta * 3
                    print(f"-> Isso equivale a {faltas_atuais} faltas no diário.")
                else:
                    faltas_atuais = int(input("Faltas atuais registradas no diário: "))
                
                if faltas_atuais < 0 or aulas_ministradas < 0:
                    print("Os valores não podem ser negativos.")
                    continue

                # O limite de 25% é sempre calculado em cima das aulas previstas no semestre
                max_faltas = math.floor(aulas_previstas * 0.25)
                faltas_restantes = max_faltas - faltas_atuais
                
                # Lógica para mostrar quantos dias completos de falta ainda restam
                dias_restantes = faltas_restantes // 3
                aulas_sobra = faltas_restantes % 3
                
                # Cálculos para bater exatamente com as métricas do Q-Acadêmico
                presenca_prevista_perc = ((aulas_previstas - faltas_atuais) / aulas_previstas) * 100
                
                if aulas_ministradas > 0:
                    presenca_ministrada_perc = ((aulas_ministradas - faltas_atuais) / aulas_ministradas) * 100
                else:
                    presenca_ministrada_perc = 100.0

                print("\n" + "="*15 + f" Status: {disciplina.upper()} " + "="*15)
                print(f"Carga da disciplina: {aulas_previstas} aulas (Limite máximo de faltas: {max_faltas})")
                print("-" * 60)
                print(f"Faltas atuais: {faltas_atuais} aula(s)")
                print(f"Faltas que ainda pode ter: {faltas_restantes} aula(s)")
                if faltas_restantes >= 3:
                    print(f"-> Isso permite faltar mais {dias_restantes} dia(s) completo(s) e {aulas_sobra} aula(s).")
                print("-" * 60)
                print(f"Presença (com base nas aulas previstas): {presenca_prevista_perc:.0f}%")
                print(f"Presença (com base nas aulas ministradas): {presenca_ministrada_perc:.0f}%")
                print("-" * 60)
                
                if faltas_restantes > 0:
                    print(f"✅ Tranquilo! Ainda há margem para {faltas_restantes} falta(s).")
                elif faltas_restantes == 0:
                    print(f"⚠️ ATENÇÃO: Limite atingido! Não é possível faltar mais nenhuma vez sem reprovar.")
                else:
                    print(f"❌ REPROVAÇÃO: O limite foi ultrapassado em {abs(faltas_restantes)} falta(s).")
                print("="*60 + "\n")
                
            except ValueError:
                print("\nErro: Por favor, digite números inteiros válidos nos campos de aulas e faltas.")
        else:
            print("\nOpção inválida. Digite 1 para calcular ou 0 para sair.")

if __name__ == "__main__":
    calculadora_faltas_qacademico()