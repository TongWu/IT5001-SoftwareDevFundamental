public class Mage extends GameCharacter {
    // public static constants
    public static final int COST = 200;

    // private static constants
    private static final String MAGE_NAME = "Mage";
    private static final String RECOVERY_FORMAT_STRING = "Mana recover to %d\n";
    private static final String CAST_FORMAT_STRING = "Strike %s with spell!\n";
    private static final int MAGE_MAX_HP = 800;
    private static final int MAGE_MAX_MANA = 50;
    private static final int MAGE_INT = 400;
    private static final int SPELL_MANA_COST = 20;
    private static final int MANA_RECOVERY = 20;

    // protected attributes. can be used by subclasses
    protected final int intelligence = MAGE_INT;

    // public constructor
    public Mage() {
        super(MAGE_NAME, MAGE_MAX_HP, MAGE_MAX_MANA);
    }

    // protected constructor
    protected Mage(String name) {
        super(name, MAGE_MAX_HP, MAGE_MAX_MANA);
    }

    // causes the mage to act. not to be overridden
    public final void act(Team myTeam, Team enemyTeam) {
        if (currentMana < SPELL_MANA_COST) {
            currentMana += MANA_RECOVERY;
            System.out.printf(RECOVERY_FORMAT_STRING, currentMana);
        } else {
            currentMana -= SPELL_MANA_COST;
            cast(myTeam, enemyTeam);
        }
    }

    // casts a spell
    protected void cast(Team myTeam, Team enemyTeam) {
        GameCharacter target = enemyTeam.getRandomLivingCharacter();
        System.out.printf(CAST_FORMAT_STRING, target);
        target.gotHurt(intelligence);
    }
}
