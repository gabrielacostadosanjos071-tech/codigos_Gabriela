import streamlit as st
### colocar um titulo
# st.title("imune ao conhecimento")

# ### escreve
# st.write("testando... esquerda ou direita ")

# ### cria uma barra lateral
# st.sidebar.title("barra lateral")

# ### criando a lista
# # nomes ficticios, qualquer semeljança é coincidencia

# nomes = ["Gabi", "Sophia", "Isa", Yasmin]

# # ## cria a caixinha na barra lateral
# st.sidebar.selectbox("escolha um nome :" , nomes)

# ## COLOCA O VIDEO NA PAGINA DO SITE
# st.video("https://www.youtube.com/watch?v=eC12XRzMH28")


st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para voce!")
carros = ["Gol", "BMW", "corsa", "toro"]



opçao = st.sidebar.selectbox("escolha o carro que foi alugado", carros)



st.title('car rental - aluguel de3 carro')

st.image(f'{opçao}.png')
st.markdown(f'## voce alugou o modelo: {opçao}')
st.markdown('---')

dias = st.text_input(f"por quantos dias o {opçao} foi alugado?")
km = st.text_input(f"quantos km voce rodou com o {opçao}?")





### copia daqui pra frente --- define a diaria
if opçao == 'BMW':
    diaria = 450

elif opçao == 'Gol':
    diaria = 350

elif opçao == 'toro':
    diaria = 500

elif opçao == 'corsa':
    diaria = 550

### calcular

if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'voce alugou o {opçao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')