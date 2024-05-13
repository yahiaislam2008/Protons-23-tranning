import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:forthapp/data.dart';
import 'package:forthapp/scrrens/Homescreen.dart';
import 'package:forthapp/scrrens/Imgprofile.dart';

class Userprofile extends StatelessWidget {
  const Userprofile({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        leading: IconButton(
            onPressed: () {
              print("ok");
              Navigator.pop(context);
            },
            icon: Icon(
              CupertinoIcons.home,
              size: 24,
            )),
        actions: [
          IconButton(
              onPressed: () {},
              icon: Icon(
                CupertinoIcons.envelope_open,
                size: 23,
              )),
          // IconButton(onPressed:(){},
          // icon: Icon(CupertinoIcons.home,
          // size: 23,)),
          IconButton(
              onPressed: () {},
              icon: Icon(
                CupertinoIcons.bell,
                size: 23,
              ))
        ],
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          imgprofile( 
            iamgeurl: currtenuser.iamgeurl,
            size: 200,
          ),
          Text(
            "Username: ${currtenuser.firstname}"
          ),
          Text(
            "Last name: ${currtenuser.lastname}"
          ),
          Text(
            "country: ${currtenuser.country}"
          )
        ],
      ),
      
    );
  }
}
