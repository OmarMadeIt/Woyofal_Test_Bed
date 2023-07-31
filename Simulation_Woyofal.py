import streamlit as st

# Fonction pour calculer la variable nb_watts
def calculate_nb_watts(montant_encours, montant_nouveau):
    seuil_1 = 14466
    seuil_2 = 28436
    redevance = 429
    TVA =0.18
    Taxe_Com = 0.025
    Prix_tranche_1 = 91.17
    Prix_tranche_2 = 136.49
    Prix_tranche_3 = 149.06
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

    conso_tranche_1 = montant_tranche_1_HT/Prix_tranche_1
    conso_tranche_2 = montant_tranche_2_HT/Prix_tranche_2
    conso_tranche_3 = montant_tranche_3_HT/Prix_tranche_3
    nb_watts = conso_tranche_1 + conso_tranche_2 + conso_tranche_3
    return nb_watts

# Interface utilisateur avec Streamlit
st.title("Simulateur Calcul Woyofal")
st.write("Veuillez préciser les renseignements ci-dessous :")
montant_encours = st.number_input("Quel est le montant total que vous avez déjà rechargé au cours de ce mois ?", value=0, step=1)
montant_nouveau = st.number_input("Combien souhaitez-vous recharger ?", value=0, step=1)

if st.button("Calculer"):
    nb_watts = calculate_nb_watts(montant_encours, montant_nouveau)
    st.write("Vous avez droit à :", nb_watts)
    