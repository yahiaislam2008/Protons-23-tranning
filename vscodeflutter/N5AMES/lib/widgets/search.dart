import 'package:flutter/material.dart';

class searchwid extends StatefulWidget {
  const searchwid({super.key});

  @override
  State<searchwid> createState() => _searchwidState();
}

class _searchwidState extends State<searchwid> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(top: 16, left: 16, right: 16),
      child: TextField(
        decoration: InputDecoration(
          hintText: "Search...",
          hintStyle: TextStyle(color: Colors.grey.shade600),
          prefixIcon: Icon(
            Icons.search,
            color: Colors.grey.shade600,
            size: 20,
          ),
          filled: true,
          fillColor: Colors.grey.shade100,
          contentPadding: EdgeInsets.all(8),
          border: OutlineInputBorder( 
              borderRadius: BorderRadius.all(Radius.circular(20)),
              borderSide: BorderSide(color: Colors.grey.shade100)),
        ),
      ),
    );
  }
}
