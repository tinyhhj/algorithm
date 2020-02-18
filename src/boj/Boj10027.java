package boj;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Boj10027 {
    static int row;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("boj/10027.txt")));
        int line = Integer.valueOf(br.readLine());
        List<Element> rootElems = new ArrayList<>();
        String[] buffer = new String[line];
        for(int i = 0 ;  i < line ; i++) {
            buffer[i] = br.readLine();
        }
        for(row = 0 ; row < buffer.length ; ) {
            rootElems.add(createElement(buffer));
        }
        line = Integer.valueOf(br.readLine());
        String[] selectors = new String[line];
        for(int i = 0 ; i < line ; i++) {
            String[] classifiers = selectors[i].split(" | > ");
//            Arrays.stream(classifiers).reduce(s->rootElems.stream().flatMap(e->e.findSelector(s)))
        }
//        rootElems.add(createElement(tag, br));
//        rootElems.forEach(e->e.findSelector());

        System.out.println(br.readLine());
    }

    public static class Element {
        String id;
        List<String> classes;
        List<Element> children;

        public Element(String id, List<String> classes, List<Element> children) {
            this.id = id;
            this.classes = classes;
            this.children = children;
        }
        public List<Element> findSelector(String selector) {
            List<Element> elements = new ArrayList<>();
            if( classes.contains(selector.substring(1))) {
                elements.add(this);
            }
            children.stream().forEach(e->elements.addAll(e.findSelector(selector)));
            return elements;
        }
    }

    public static Element createElement(String[] buffer) throws IOException {
        String[] idClasses = buffer[row++].split(" ");
        String id = idClasses[1].substring(4,idClasses[1].length());
        List<String> classes = new ArrayList<>();
        List<Element> children = new ArrayList<>();
        if( idClasses.length == 3 ) {
            if(!idClasses[2].endsWith("''>")) {
                classes.add(idClasses[2].substring(7,idClasses[2].length()-2));
            }
        } else if(idClasses.length == 4) {
            classes.add(idClasses[2].substring(7,idClasses[2].length()));
            classes.add(idClasses[3].substring(0,idClasses[3].length()-2));
        } else {
            classes.add(idClasses[2].substring(7,idClasses[2].length()));
            for(int j = 0 ; j < idClasses.length - 4; j++) {
                classes.add(idClasses[j+3]);
            }
            classes.add(idClasses[idClasses.length-1].substring(0,idClasses[idClasses.length-1].length()-2));
        }
        String nextTag = buffer[row++];
        while(row < buffer.length) {
            if( nextTag.startsWith("</")) {
                return new Element(id, classes , children);
            } else {
                children.add(createElement(buffer));
            }
            nextTag = buffer[row++];
        }
        return null;
    }

}
