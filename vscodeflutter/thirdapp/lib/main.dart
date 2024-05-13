import 'package:flutter/material.dart';

//if there is somthing overflow u can use expaneded to make it fit
//flotbutton=textbutton , RaisedButton =ElevatedButton , OutlineButton = OutlinedButton
//To make a the color design make style
//for each button u should do onpressedbutton there is also onlong pressed button
// u can live the one pressedbutton null it will stop working u can her style by onsurface
//to make something clickable like an image for ex we use a widget called GestureDetector
// to create a stateless widget do stless for stateful do stful

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int numb =12;
  Color colbot = Colors.lightBlue;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            setState(() {
              numb ++;
              colbot = Colors.deepOrange;
            });
            print("it's ok");
          },
          child: Icon(Icons.add),
          backgroundColor: Colors.cyanAccent,
        ),
        body: Column(
          children: [
            Row(
              children: [
                Expanded(
                    child: GestureDetector(
                      onDoubleTap: () {
                        print("image is pressed");
                      },
                      child: Image(
                          image: AssetImage("image/proyahia.jpg"),
                                    ),
                    )),
                // Expanded(
                //     child: Image(
                //   image: AssetImage("image/proyahia.jpg"),
                // )),
              ],
            ),
            Text(
                "$numb",
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.green,
                ),
            ),
            TextButton(
              onPressed: (){
                setState(() {
                  colbot= Colors.green;
                  numb +=1;  
                });
                
                print("button is pressed");
                print("your number is $numb");
                print("your color is $colbot");
                //my number when i click the icon is plusing one put it is not 
                //showing us because we are in a stateless widget
                //so we now when we change it to a stateful it doesnot going to work so we have to use sestate
              },
              child: Icon(Icons.ac_unit_outlined,
              color: colbot,
              size: 26),

              ),
            // FloatingActionButton(
            //   onPressed: () {
            //     print("it's ok");
            //   },
            //   child: Icon(
            //     Icons.check,
            //     size: 20,
            //   ),
            //   backgroundColor: Colors.amberAccent,
            // ),
            // ElevatedButton.icon(
            //   onPressed: () {
            //     print("sfkox;lcdvk;lvsd,");
            //   },
            //   style: ElevatedButton.styleFrom(
            //       backgroundColor: Colors.black,
            //       foregroundColor: Colors.amber,
            //       textStyle: TextStyle(
            //         fontSize: 30,
            //       ),
            //       padding: EdgeInsets.all(20)),
            //   label: Text("efhkdfvh"),
            //   icon: Icon(Icons.access_alarm),
            //   onLongPress: () {
            //     print("do not do that");
            //   },
            // ),
            // ElevatedButton.icon(
            //   onPressed: null, //() {
            //   //   print("sfkox;lcdvk;lvsd,");
            //   // },
            //   label: Text("kjh"),
            //   icon: Icon(Icons.access_alarm),
            //   style: ElevatedButton.styleFrom(
            //     primary: Colors.deepOrangeAccent,
            //     onPrimary: Colors.deepPurple,
            //     onSurface: Colors.blueGrey,
            //   ),

            //   onLongPress: () {
            //     print("do not do that");
            //   },
            // ),
            // TextButton(
            //   style: ButtonStyle(),
            //   onPressed: () {},
            //   child: Text('TextButton'),
            // ),
            // OutlinedButton(
            //   onPressed: () {},
            //   child: Text("vkfjd;l"),
            //   style: OutlinedButton.styleFrom(
            //     primary: Colors.blueAccent,
            //     side: BorderSide(color: Colors.red ,width: 12)
            //   ), 
            //   )
          ],
        ),
      ),
    );
  }
}
