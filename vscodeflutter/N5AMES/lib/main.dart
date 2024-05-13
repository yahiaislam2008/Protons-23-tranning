import 'package:flutter/material.dart';
import 'package:n5ames/screens/login.dart';
void main() {
  runApp(const MyApp());
}
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}
class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "N5ames",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        appBarTheme: AppBarTheme(backgroundColor:Color(0xFFFFA726) ),
        scaffoldBackgroundColor: Color(0xFFFFA726),
        primarySwatch: Colors.blue,
        iconTheme: IconThemeData(color: Colors.purpleAccent),

      ),
      home: LoginScreen(),
    );
  }
}


