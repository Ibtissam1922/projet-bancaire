import streamlit as st
import pandas as pd
from compte import Compte, gestioncompte
st.set_page_config(
    page_title="Gestion d'un system bancaire simplifie",
    layout="wide"
)

# Conserver les données entre les interactions
#session_state pour conserver l’objet gestionEtudiant"
if "gestion" not in st.session_state:
    st.session_state.gestion = gestioncompte()

gestion = st.session_state.gestion
st.title("Gestion d'un Système Bancaire Simplifié")

menu = st.sidebar.selectbox(
    "Choisissez une opération",
    [
        "Création du compte",
        "Déposer de l'argent",
        "Retirer de l'argent",
        "Virement",
        "Consulter le solde",
        "Afficher les comptes",
        "Historique des opérations"
    ]
)
# ======================creer le compte=============================
if menu == "Création du compte":

    st.header("Création d'un compte")

    numc= st.number_input("num", min_value=1, step=1)
    nom = st.text_input("Nom")
    solde = st.number_input("solde initial")

    if st.button("Creer"):
        try:

            c = Compte(int(numc), nom, float(solde))
            c.creer()
            gestion.ajouterCompte(c)
            st.success("compte creer avec succès.")

        except Exception as ex:
            st.error(f"Erreur : {ex}")

# ======================deposer dans le compte=============================
elif menu == "Déposer de l'argent":

    st.header("Dépôt")

    num = st.text_input("Numéro du compte")
    montant = st.number_input("Montant", min_value=0.0)

    if st.button("Déposer"):

        compte = gestion.chercherCompte(num)

        if compte:
            compte.deposerArgent(montant)
            st.success("Dépôt effectué.")
        else:
            st.error("Compte introuvable.")
# ======================retirer d un montant de compte=============================
elif menu == "Retirer de l'argent":

    st.header("Retrait")

    num = st.text_input("Numéro du compte")
    montant = st.number_input("Montant", min_value=0.0)

    if st.button("Retirer"):

        compte = gestion.chercherCompte(num)

        if compte:
            compte.retirerArgent(montant)
            st.success("Retrait effectué.")
        else:
            st.error("Compte introuvable.")

# ======================Virement=============================
elif menu == "Virement":

    st.header("Virement")

    source = st.text_input("Compte source")
    destination = st.text_input("Compte destinataire")
    montant = st.number_input("Montant", min_value=0.0)

    if st.button("Effectuer le virement"):

        c1 = gestion.chercherCompte(source)
        c2 = gestion.chercherCompte(destination)

        if c1 and c2:
            c1.virement(c2, montant)
            st.success("Virement effectué.")
        else:
            st.error("Compte introuvable.")

# ======================consultation du solde =============================
elif menu == "Consulter le solde":

    st.header("Consulter le solde")

    num = st.text_input("Numéro du compte")

    if st.button("Consulter"):

        compte = gestion.chercherCompte(num)

        if compte:
            st.info(f"Solde : {compte.getSolde()} DH")
        else:
            st.error("Compte introuvable.")

# =====================affichage de liste des comptes =============================

elif menu == "Afficher les comptes":

    st.header("Liste des comptes")

    comptes = gestion.getComptes()

    if comptes:

        data = []

        for c in comptes:
            data.append({
                "Numéro": c.getNumc(),
                "Titulaire": c.getNomt(),
                "Solde": c.getSolde()
            })

        st.dataframe(data)

    else:
        st.warning("Aucun compte.")
# ======================historique des opération =============================
elif menu == "Historique des opérations":

    st.header("Historique")

    num = st.text_input("Numéro du compte")

    if st.button("Afficher"):

        compte = gestion.chercherCompte(num)

        if compte:

            for op in compte.getHistorique():
                st.write(op)

        else:
            st.error("Compte introuvable.")
