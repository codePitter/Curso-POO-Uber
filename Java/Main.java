package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Inicializando");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123", "ann@gmail.com", "123456"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH123", new Account("Andres Herrera", "AND123", "ann@gmail.com", "123456"));
        uberVan.setPassegenger(6);
        uberVan.printDataCar();

        // System.out.println("Uberx....");
        // UberX uberX = new UberX("DFG579", new Account("Pedro Quiroga", "123456", "pedro@gmail.xom", "123578"), "Ford", "Focus");
    }
}