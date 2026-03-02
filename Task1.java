import java.util.*;

public class Task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome to Chatbot");
        Response re = new Response();

        while (true) {
            String userInput = sc.nextLine();
            if ("exit".equalsIgnoreCase(userInput)) {
                System.out.println("Thank You see you later!");
                break;
            }
            re.respond(userInput);
        }
        sc.close();
    }
}

class Response {
    private final String allData =
        "Chatbot: Hello! How can I help you?," +
        "There is a virtual Internship available in Codsoft," +
        "I am digital source I am always free to chat you!," +
        "Today's weather is sunny with a chance of rain.," +
        "We offer internships in various domains including software development data science and Artificial Intelligent.," +
        "Their office is located in TamilNadu.," +
        "Chatbot: I am just a program, but I am here to help!," +
        "Chatbot: Why don't programmers like nature? It has too many bugs.," +
        "Chatbot: CodSoft is a company providing internships and skill development programs.," +
        "Chatbot: Data Science and Artificial Intelligence are trending domains to explore.";

    public void respond(String userInput) {
        System.out.println("User: " + userInput);

        String[] responses = allData.split(",");
        for (String response : responses) {
            if (matchesResponse(userInput, response)) {
                System.out.println(response);
                return;
            }
        }
        System.out.println("Chatbot: I did not understand that. Can you please clarify?");
    }

    private boolean matchesResponse(String userInput, String response) {
        if ("hello".equalsIgnoreCase(userInput) && response.startsWith("Chatbot")) {
            return true;
        }
        if ("I want do internship".equalsIgnoreCase(userInput) && response.startsWith("There")) {
            return true;
        }
        if ("Are you free to chat".equalsIgnoreCase(userInput) && response.startsWith("I am digital")) {
            return true;
        }
        if ("what's the weather like".equalsIgnoreCase(userInput) && response.startsWith("Today")) {
            return true;
        }
        if ("what internships are available".equalsIgnoreCase(userInput) && response.startsWith("We offer")) {
            return true;
        }
        if ("where is codSoft office located".equalsIgnoreCase(userInput) && response.startsWith("Their office")) {
            return true;
        }
        if ("how are you?".equalsIgnoreCase(userInput) && response.startsWith("Chatbot: I am just a program")) {
            return true;
        }
        if ("tell me a joke".equalsIgnoreCase(userInput) && response.startsWith("Chatbot: Why don't programmers")) {
            return true;
        }
        if ("what is codSoft?".equalsIgnoreCase(userInput) && response.startsWith("Chatbot: CodSoft is a company")) {
            return true;
        }
        if ("can you suggest a domain to learn?".equalsIgnoreCase(userInput) && response.startsWith("Chatbot: Data Science")) {
            return true;
        }
        return false;
    }
}
