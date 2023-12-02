public class Fighter extends GameCharacter {
    // public static constants
    public static final int COST = 100;

    // private static constants
    private static final int FIGHTER_MAX_HP = 1200;
    private static final int FIGHTER_MAX_MANA = 0;
    private static final int FIGHTER_STR = 100;
    private static final String FIGHTER_NAME = "Fighter";
    private static final String ACT_FORMAT_STRING = "Attack %s with %d damage!\n";

    // protected attributes
    protected final int strength = FIGHTER_STR;

    // Creates a fighter
    public Fighter() {
        super(FIGHTER_NAME, FIGHTER_MAX_HP, FIGHTER_MAX_MANA);
    }

    // Creates a fighter of another name
    protected Fighter(String name) {
        super(name, FIGHTER_MAX_HP, FIGHTER_MAX_MANA);
    }

    // returns the damage dealt by this fighter
    protected int damage() {
        return strength;
    }

    // causes the fighter to act. not to be overridden
    public final void act(Team myTeam, Team enemyTeam) {
        GameCharacter target = enemyTeam.getRandomLivingCharacter();
        int damage = damage();
        System.out.printf(ACT_FORMAT_STRING, target, damage);
        target.gotHurt(damage);
    }
}
