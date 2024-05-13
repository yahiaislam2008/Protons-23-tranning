import 'package:flutter/material.dart';

//MaterialApp for compontes
// then "," comma after widget
// and we have center and for her parametr is child: then text or iamge
//scaffold has many propirties|>
//appbar probrtes we have (title:the text),(backgrondcolor:the color,[]for درجة اللون ) this for app bar
// for just the app as normal in scaffold
// u have for contant body :contant DO NOT FORGET
//prefer iamge.png to put an image u have on the pc u have to go to th pubspec.yamel then u
//will find somthing that called assert that u have to put file image
//prefer image.png to put an image a image form link from child: Image(image: NetworkImage(link))
//to make an icon app to app genrator the picter then extract then from the prject file
//androd then app then scr then main res  show in explor
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('Sleeping'),
        backgroundColor: Colors.deepPurpleAccent[900],
      ),
      backgroundColor: Colors.green,
      body: Center(
        child: Image(image: AssetImage('images/proyahia.jpg')),
      ),
    ),
  ));
}
