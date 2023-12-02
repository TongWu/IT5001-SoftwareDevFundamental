import java.util.ArrayList;
import java.util.Random;
import java.util.function.Predicate;

/** A team of characters in a game */
public final class Team {
    // private static constants
    private static final String ALIVE = "alive";
    private static final String DEAD = "dead";
    private static final String EXCEPTION_FORMAT_STRING = "None of the characters in this team are %s!";
    private static final String MEMBERS = "Members";
    private static final String HITPOINTS = "Hitpoints";
    private static final String MANA = "Mana";
    private static final String STATUS = "Status";
    private static final String WHITESPACE = " ";
    private static final String HLINE_DELIM = "+";
    private static final String HLINE_CHAR = "-";
    private static final String COL_DELIM = " | ";
    private static final String STAT_FORMAT_STRING = "%d / %d";
    private static final int HEADER_LENGTH = StringOps.maxLength(new String[] {MEMBERS, HITPOINTS, MANA, STATUS});
    private static final String NAMES_ROW_HEADER = StringOps.padTo(MEMBERS, HEADER_LENGTH, WHITESPACE);
    private static final String HEADER_HLINE = HLINE_CHAR.repeat(HEADER_LENGTH);
    private static final String HP_ROW_HEADER = StringOps.padTo(HITPOINTS, HEADER_LENGTH, WHITESPACE);
    private static final String MP_ROW_HEADER = StringOps.padTo(MANA, HEADER_LENGTH, WHITESPACE);
    private static final String ALIVE_ROW_HEADER = StringOps.padTo(STATUS, HEADER_LENGTH, WHITESPACE);

    // private attributes
    private final Random rng;
    private final ArrayList<GameCharacter> members = new ArrayList<>();

    // constructors
    /**
     * Creates an empty team
     * @param r the random generator
     */
    public Team(Random r) {
        rng = r;
    }

    /**
     * Adds a member to the team
     * @param c the new member to add
     */
    public void addMember(GameCharacter c) {
        members.add(c);
    }

    /**
     * Determines if everyone in the team is alive
     * @return true if everyone in the team is alive, false otherwise
     */
    public boolean isAllAlive() {
        return getAllDeadCharacters().length == 0;
    }

    /**
     * Determines if everyone in the team is dead
     * @return true if everyone in the team is dead, false otherwise
     */
    public boolean isAllDead() {
        return getAllLivingCharacters().length == 0;
    }

    /**
     * Gets a random character in the team who is still alive
     * @return the random living character
     */
    public GameCharacter getRandomLivingCharacter() {
        return getRandomCharacterOfPredicate(ALIVE, x -> x.isAlive());
    }

    /**
     * Gets all characters in the team who are still alive
     * @return all characters in the team who are still alive
     */
    public GameCharacter[] getAllLivingCharacters() {
        return filterCharacters(x -> x.isAlive());
    }

    /**
     * Gets a random character in the team who is dead
     * @return a random dead character
     */
    public GameCharacter getRandomDeadCharacter() {
        return getRandomCharacterOfPredicate(DEAD, x -> !x.isAlive());
    }

    /**
     * Gets all characters in the team who are dead
     * @return all characters in the team who are dead
     */
    public GameCharacter[] getAllDeadCharacters() {
        return filterCharacters(x -> !x.isAlive());
    }
    
    private GameCharacter getRandomCharacterOfPredicate(String type, Predicate<GameCharacter> p) {
        GameCharacter[] characters = filterCharacters(p);
        if (characters.length == 0)
            throw new RuntimeException(String.format(EXCEPTION_FORMAT_STRING, type));
        return characters[rng.nextInt(characters.length)];
    }

    private GameCharacter[] filterCharacters(Predicate<GameCharacter> p) {
        return members
            .stream()
            .filter(p)
            .toArray(GameCharacter[]::new);
    }

    @Override
    public String toString() {
        ArrayList<String> names = new ArrayList<>();
        names.add(NAMES_ROW_HEADER);
        ArrayList<String> hline = new ArrayList<>();
        hline.add(HEADER_HLINE);
        ArrayList<String> hp = new ArrayList<>();
        hp.add(HP_ROW_HEADER);
        ArrayList<String> mp = new ArrayList<>();
        mp.add(MP_ROW_HEADER);
        ArrayList<String> alive = new ArrayList<>();
        alive.add(ALIVE_ROW_HEADER);
        for (GameCharacter c : members) {
            String charName = c.toString();
            String charHp = String.format(STAT_FORMAT_STRING, c.currentHp(), c.maxHp());
            String charMp = String.format(STAT_FORMAT_STRING, c.currentMana(), c.maxMana());
            String status = c.getStatus();
            int columnLength = StringOps.maxLength(new String[]{
                charName, charHp, charMp, status
            });
            names.add(StringOps.padTo(charName, columnLength, WHITESPACE));
            hline.add(HLINE_CHAR.repeat(columnLength));
            hp.add(StringOps.padTo(charHp, columnLength, WHITESPACE));
            mp.add(StringOps.padTo(charMp, columnLength, WHITESPACE));
            alive.add(StringOps.padTo(status, columnLength, WHITESPACE));
        }
        String line = String.join(HLINE_CHAR + HLINE_DELIM + HLINE_CHAR, hline);
        return line + "\n" +
            String.join(COL_DELIM, names) + "\n" +
            String.join(COL_DELIM, hp) + "\n" +
            String.join(COL_DELIM, mp) + "\n" +
            String.join(COL_DELIM, alive) + "\n" +
            line;
    }


    private static interface StringOps {
        static String padTo(String s, int padding, String pad) {
            StringBuilder sb = new StringBuilder(s);
            for (int i = sb.length(); i < padding; ++i) {
                sb.append(pad);
            }
            return sb.toString();
        }
        static int maxLength(String[] args) {
            int max = -1;
            for (String s : args)
                if (s.length() > max)
                    max = s.length();
            return max;
        }
    }
}