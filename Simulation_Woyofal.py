import streamlit as st

# Fonction pour calculer la variable nb_watts
def calculate_nb_watts(montant_encours, montant_nouveau, seuil_1, seuil_2, Prix_tranche_1, Prix_tranche_2, Prix_tranche_3):
    #seuil_1 = 14466
    #seuil_2 = 28436
    redevance = 429
    TVA =0.18
    Taxe_Com = 0.025
    #Prix_tranche_1 = 91.17
    #Prix_tranche_2 = 136.49
    #Prix_tranche_3 = 149.06
    cumul = montant_nouveau+montant_encours

    if cumul < seuil_1:
        montant_tranche_1 = montant_nouveau
        montant_tranche_2 = 0
        montant_tranche_3 = 0
    elif cumul<= seuil_2 and cumul> seuil_1 and montant_encours <= seuil_1:
        montant_tranche_1 = seuil_1 - montant_encours
        montant_tranche_2 = cumul - seuil_1
        montant_tranche_3 = 0
    elif cumul<= seuil_2 and cumul> seuil_1 and montant_encours > seuil_1:
        montant_tranche_1 = 0
        montant_tranche_2 = montant_nouveau
        montant_tranche_3 = 0
    elif cumul > seuil_2 and montant_encours<=seuil_1:
        montant_tranche_1 = seuil_1 - montant_encours
        montant_tranche_2 = seuil_2 - seuil_1
        montant_tranche_3 = cumul - seuil_2
    elif cumul > seuil_2 and montant_encours>seuil_1 and montant_encours<= seuil_2:
        montant_tranche_1 = 0
        montant_tranche_2 = seuil_2 - montant_encours
        montant_tranche_3 = cumul - seuil_2
    elif cumul > seuil_2 and montant_encours>seuil_2:
        montant_tranche_1 = 0
        montant_tranche_2 = 0
        montant_tranche_3 = montant_nouveau
    else:
        montant_tranche_1 = 0

    print(montant_tranche_1)
    print(montant_tranche_2)
    print(montant_tranche_3)

    if montant_encours==0:
        montant_tranche_1_HT = montant_tranche_1-redevance-(montant_tranche_1*Taxe_Com)
    else :
        montant_tranche_1_HT = montant_tranche_1-montant_tranche_1*Taxe_Com

    montant_tranche_2_HT = montant_tranche_2-montant_tranche_2*Taxe_Com
    montant_tranche_3_HT = montant_tranche_3-montant_tranche_3*Taxe_Com-montant_tranche_3*TVA

    conso_tranche_1 = round(montant_tranche_1_HT/Prix_tranche_1,2)
    conso_tranche_2 = round(montant_tranche_2_HT/Prix_tranche_2,2)
    conso_tranche_3 = round(montant_tranche_3_HT/Prix_tranche_3,2)
    nb_watts = conso_tranche_1 + conso_tranche_2 + conso_tranche_3
    return nb_watts, conso_tranche_1, conso_tranche_2, conso_tranche_3

# Interface utilisateur avec Streamlit
st.title("Simulateur Calcul Woyofal")
st.write("Veuillez choisir le type de foyer :")
foyer_type = st.selectbox("Sélectionnez le type de foyer :", ["DPP (Domestique Petite Puissance)", "DMP (Domestique Moyenne Puissance)"])

if foyer_type == "DPP (Domestique Petite Puissance)":
    seuil_1 = 14466
    seuil_2 = 28436
    Prix_tranche_1 = 91.17
    Prix_tranche_2 = 136.49
    Prix_tranche_3 = 149.06
    
elif foyer_type == "DMP (Domestique Moyenne Puissance)":
    seuil_1 = 7127
    seuil_2 = 43909
    Prix_tranche_1 = 111.23
    Prix_tranche_2 = 143.54
    Prix_tranche_3 = 150.23
    
st.write("Veuillez préciser les renseignements ci-dessous :")
#montant_encours = st.number_input("Quel est le montant total que vous avez déjà rechargé au cours de ce mois ?", value=0, step=1)
montant_encours = st.slider("Quel est le montant total que vous avez déjà rechargé au cours de ce mois ?", min_value=0, max_value=100000, step=500, value=0)

#montant_nouveau = st.number_input("Combien souhaitez-vous recharger ?", value=0, step=1)
montant_nouveau = st.slider("Combien souhaitez-vous recharger ?", min_value=0, max_value=100000, step=500, value=0)

if st.button("Calculer"):
    nb_watts, conso_tranche_1, conso_tranche_2, conso_tranche_3=calculate_nb_watts(montant_encours,montant_nouveau, seuil_1, seuil_2, Prix_tranche_1, Prix_tranche_2, Prix_tranche_3)
    st.write("Vous avez droit à :", nb_watts)
    st.write("Détails")
    st.write("Puissance Tranche 1 :", conso_tranche_1)
    st.write("Puissance Tranche 2 :", conso_tranche_2)
    st.write("Puissance Tranche 3 :", conso_tranche_3)
    