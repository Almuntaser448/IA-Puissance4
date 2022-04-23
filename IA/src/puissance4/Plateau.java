package puissance4;

import java.util.ArrayList;
import java.util.Iterator;

public class Plateau {
	private Case[][] plateau = new Case[7][6];
	private ArrayList<Case> casesJouable;

	public Plateau() {
		casesJouable = new ArrayList<Case>();
		for (int i = 0; i < 7; i++) {
			for (int y = 0; y < 6; y++) {
				plateau[i][y] = new Case(i, y, Couleur.Vide);
				if (i == 0) {
					casesJouable.add(plateau[i][y]);
				}
			}
		}
	}

	public Case[][] getPlateau() {
		return plateau;
	}

	public void jouerCase(Case c, Couleur couleur) {

			this.casesJouable.remove(c);
			c.setCouleur(couleur);
			if (c.getPositionY() != 5) {
				this.casesJouable.add(plateau[c.getPositionX() ][c.getPositionY()+1]);
			}

	}

	public void startGame() {
		Joueur joueur1 = new Jhumain("", Couleur.Rouge);
		Joueur joueur2 = new Jhumain("", Couleur.Jaune);

		while (!gameFinished()) {
			Case c = joueur1.jouer(casesJouable);
			jouerCase(c, joueur1.getCouleur());
		}
	}

	private boolean gameFinished() {
		if (casesJouable.size() == 0) {
			return true;
		}
		// Not complete
	}

	private boolean checkIfWinVertical() {
		for (int i = 0; i < 7; i++) {
			Couleur lastCouleur = Couleur.Vide;
			int count = 0;
			for (int y = 0; y < 6; y++) {
				if (plateau[i][y].getCouleur() != lastCouleur) {
					lastCouleur = plateau[i][y].getCouleur();
					count = 0;
				}
				count += 1;
			}
			if (count >= 4) {
				return true;
			}
		}
		return false;
	}

	private boolean checkIfWinHorizontal() {
		for (int y = 0; y < 6; y++) {
			Couleur lastCouleur = Couleur.Vide;
			int count = 0;
			for (int i = 0; i < 7; i++) {
				if (plateau[i][y].getCouleur() != lastCouleur) {
					lastCouleur = plateau[i][y].getCouleur();
					count = 0;
				}
				count += 1;
			}
			if (count >= 4) {
				return true;
			}
		}
		return false;
	}
	
	private boolean checkIfWinDiagonale1(){
		for (int y = 0; y < 6; y++) {
			Couleur lastCouleur = Couleur.Vide;
			int count = 0;
			for (int i = 0; i < 7; i++) {
				if (plateau[i][y].getCouleur() != lastCouleur) {
					lastCouleur = plateau[i][y].getCouleur();
					count = 0;
				}
				count += 1;
			}
			if (count >= 4) {
				return true;
			}
		}
		return false;
	}
	
	private boolean checkIfWinDiagonale2(){
		
	}

	public int evaluation() {
		// TO DO
	}

}
