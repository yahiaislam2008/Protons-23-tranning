import 'package:flutter/material.dart';

class imgprofile extends StatelessWidget {
  final String iamgeurl ;
  final double size;

  const imgprofile({
    Key ? key,
    required this.iamgeurl,
    required this.size,
  }):super(key:key);
  

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: ClipRRect(
          borderRadius: BorderRadius.circular(size/2 - size / 10),
          child: Image.network(
            iamgeurl,
            width: size,
            height: size,
            fit: BoxFit.cover,
          ),
        ),
      ) ,
    );
  }
}