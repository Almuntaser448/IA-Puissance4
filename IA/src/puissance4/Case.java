package puissance4;

public class Case {
	private int positionX, positionY;
	private Couleur couleur;

	public Case(int positionX, int positionY, Couleur couleur) {
		this.positionX = positionX;
		this.positionY = positionY;
		this.couleur = couleur;
	}

	public int getPositionX() {
		return positionX;
	}

	public int getPositionY() {
		return positionY;
	}

	public Couleur getCouleur() {
		return couleur;
	}

	public void setCouleur(Couleur couleur) {
		this.couleur = couleur;
	}

}
