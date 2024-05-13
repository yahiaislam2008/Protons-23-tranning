import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:n5ame/screens/login.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "new project",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        appBarTheme: AppBarTheme(backgroundColor:Color(0xFF795548) ),
        scaffoldBackgroundColor: Color(0xFF795548),
        primarySwatch: Colors.blue,
        iconTheme: IconThemeData(color: Colors.purpleAccent),
        fontFamily: GoogleFonts.montserrat().fontFamily,
        textTheme: GoogleFonts.montserratTextTheme(),
      ),
      home: LoginScreen(),
    );
  }
}


