
public class Cancion {
	String Artista;
	String Cancion;
	int Reproducciones;

	public Cancion(String artista, String cancion) {
		super();
		Artista = artista;
		Cancion = cancion;
		Reproducciones = 0;
	}

	void reproduccion() {
		Reproducciones+=1;
	}

	@Override
	public String toString() {
		return "Cancion [Artista=" + Artista + ", Cancion=" + Cancion + ", Reproducciones=" + Reproducciones + "]";
	}

}
