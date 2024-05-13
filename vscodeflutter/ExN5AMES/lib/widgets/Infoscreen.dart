import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:n5ame/screens/login.dart';

class Infopage extends StatelessWidget {
  const Infopage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
      elevation: 0,
        leading: IconButton(
            onPressed: () {
              print("ok");
              Navigator.of(context).push(
                MaterialPageRoute(
                  fullscreenDialog: true,
                  builder: (_) => LoginScreen(),)
                  );
            }, 
            icon: Icon(
            CupertinoIcons.back,
            size: 24,
            color: Colors.black,
            )),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Card(
            child: Padding(
              padding: EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "It is an app that we made it for :"
                  ),
                  Text(
                    "   1. Eat new food"
                  ),
                  Text(
                    "   2. Make new frinds"
                  ),
                  Text(
                    " and their is more so go and see it by your self"
                  ),
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}