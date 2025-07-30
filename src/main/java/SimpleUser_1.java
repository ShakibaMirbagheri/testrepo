Here's an example of a Java class with proper class structure and imports:
```java
public class MyClass {
    String uuid;
    String name;
    String surname;
    public MyClass(String uuid, String name, String surname) {
        this.uuid = uuid;
        this.name = name;
        this.surname = surname;
    }
    public void print() throws IOException {
        System.out.println("Hello, " + name + "!");
    }
}
```