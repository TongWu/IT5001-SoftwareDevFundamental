/**
 * A character in a game.
 */
public abstract class GameCharacter {
    // static constants/attributes
    private static int numCharacters = 0;
    private static final String ALIVE = "ALIVE";
    private static final String DEAD = "DEAD";
    private static final String DEATH_FORMAT_STRING = "%s died!\n";
    private static final String HURT_FORMAT_STRING = "%s hurt with remaining HP %d\n";
    private static final String REVIVAL_FORMAT_STRING = "%s revived with hp %d\n";
    private static final String TOSTRING_FORMAT = "%s %d";

    // protected constants/attributes (accessible by subclasses)
    protected final String name;
    protected final int maxHp;
    protected final int maxMana;
    protected final int id;
    protected int currentHp;
    protected int currentMana;
    protected boolean isAlive = true;

    // constructors
    /**
     * Creates a game character
     * @param name  the name of the character
     * @param maxHp the max HP of the character
     * @param maxMana the max MP of the character
     */
    protected GameCharacter(String name, int maxHp, int maxMana) {
        this.name = name;
        this.maxHp = this.currentHp = maxHp;
        this.maxMana = this.currentMana = maxMana;
        this.id = ++numCharacters;
    }

    // public methods

    /**
     * What to do when it is this character's turn to act
     * @param myTeam    this character's team
     * @param enemyTeam the enemy team
     */
    // Implementing classes should override this method
    public abstract void act(Team myTeam, Team enemyTeam);

    /**
     * Causes this character to receive some damage
     * @param damage the damage this character receives
     */
    public final void gotHurt(int damage) {
        if (damage >= this.currentHp) {
            // this character dies
            this.currentHp = 0;
            this.isAlive = false;
            System.out.printf(DEATH_FORMAT_STRING, this);
        } else {
            // still alive
            this.currentHp -= damage;
            System.out.printf(HURT_FORMAT_STRING, this, this.currentHp);
        }
    }

    /**
     * Revives this character with some penalty (e.g. a penalty of 0.3 will cause this
     * character to revive with only 70% of max HP)
     * @param penalty   the HP penalty from revival
     */
    public final void revive(double penalty) {
        if (isAlive)
            throw new RuntimeException("This character is already alive!");
        isAlive = true;
        currentHp = (int) (maxHp * (1 - penalty));
        System.out.printf(REVIVAL_FORMAT_STRING, this, currentHp);
    }

    // getters
    public final boolean isAlive() { return isAlive; }
    public final int currentHp() { return currentHp; }
    public final int currentMana() { return currentMana; }
    public final int maxHp() { return maxHp; }
    public final int maxMana() { return maxMana; }
    public final String getStatus() {
        if (isAlive()) return ALIVE;
        return DEAD;
    }

    @Override
    public String toString() {
        return String.format(TOSTRING_FORMAT, this.name, this.id);
    }
}
