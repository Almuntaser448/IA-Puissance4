package puissance4;

import java.util.ArrayList;
import java.util.Scanner;

public class Jhumain extends Joueur {
	public Jhumain(String n, Couleur c) {
		super(n, c);
	}

	@Override
	public Case jouer(ArrayList<Case> opitionJouable) {
		int i, y;
		boolean bonPosistion = false;
		System.out.println("C'est a vous");
		System.out.println("Vous pouvez Jouer aux cases suivantes:");
		for (Case c : opitionJouable) {
			System.out.println("le case : " + c.getPositionX() + " : " + c.getPositionY());
		}
		Scanner sc = new Scanner(System.in);

		do {
			System.out.println("Merci de bien indiquer les cordones de la case que vous voulez choisir");
			System.out.println(" sa position en horizontal (1 est la premier ligne de jeu et 7 est le dernier");
			i = sc.nextInt() - 1;// try catch apres
			System.out.println(" sa position en vertical (1 est la premier collones a gauche  et 6 est le dernier");
			y = sc.nextInt() - 1;
			for (Case c : opitionJouable) {
				if (c.getPositionX() == i && c.getPositionY() == y) {
					bonPosistion = true;
					return c;
				}
			}
		} while (!bonPosistion);
		sc.close();
		return null;
	}

}
