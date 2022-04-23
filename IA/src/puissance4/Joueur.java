package puissance4;

import java.util.ArrayList;

public abstract class Joueur { // peut etre interface
	private String nom;
	private Couleur couleur;
	
	public Joueur(String n,Couleur c ) {
		this.nom=n;
		this.couleur=c;
	}
	public String getNom() {
		return nom;
	}

	public Couleur getCouleur() {
		return couleur;
	}


	public Case jouer(ArrayList<Case> opitionJouable ) {
		return null;};
}
