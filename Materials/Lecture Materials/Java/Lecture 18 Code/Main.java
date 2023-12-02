public class Main {
    public static void main(String[] args) {
        // Create a POS that we can use
        POS p = new POS();
        // Create some orders that we can add to the POS
        AlaCarteBurger b = new AlaCarteBurger("BVPB");
        Meal m = new Meal(new AlaCarteBurger("BCPVOM"), Meal.SMALL);
        p.addOrder(b);
        p.addOrder(m);
        p.printOrders();
    }
}
