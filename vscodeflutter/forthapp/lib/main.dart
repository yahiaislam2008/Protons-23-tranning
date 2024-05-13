import 'package:flutter/material.dart';
import 'package:forthapp/contastans.dart';
import 'package:forthapp/scrrens/Homescreen.dart';
import 'package:google_fonts/google_fonts.dart';
//to theme every thing we use theme in it we use datatheme then theme every hting u want
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "new project",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        appBarTheme: AppBarTheme(backgroundColor:KBagroundcolor ),
        scaffoldBackgroundColor: KBagroundcolor,
        primarySwatch: Colors.blue,
        iconTheme: IconThemeData(color: Colors.purpleAccent),
        // primaryColor: Colors.green,
        // iconTheme: IconThemeData(color: Colors.deepOrange),
        fontFamily: GoogleFonts.montserrat().fontFamily,
        textTheme: GoogleFonts.montserratTextTheme(),
        colorScheme: ColorScheme.fromSwatch().copyWith(secondary: KAccentcolor),
      ),
      home: Homescreen(),
    );
  }
}
//login and regust and chat and matiching and recipe teo part one for ingradetnt and zabt wcalmny like dodel 