public class AlaCarteBurger implements Order {
    private String ingredients;

    public AlaCarteBurger(String ingredients) {
        this.ingredients = ingredients;
    }

    public int getPrice() {
        int price = 0;
        for (int i = 0; i < ingredients.length(); ++i) {
            if (ingredients.charAt(i) == 'B')
                price += 50;
            else if (ingredients.charAt(i) == 'M')
                price += 90;
            else if (ingredients.charAt(i) == 'P')
                price += 150;
            else if (ingredients.charAt(i) == 'V')
                price += 70;
            else if (ingredients.charAt(i) == 'O')
                price += 40;
            else if (ingredients.charAt(i) == 'C')
                price += 80;
        }
        return price;
    }

    // similar to __str__ in python
    @Override
    public String toString() {
        return String.format("Burger %s", ingredients);
    }
}
