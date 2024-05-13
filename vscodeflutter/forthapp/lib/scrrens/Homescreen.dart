import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:forthapp/data.dart';
import 'package:forthapp/scrrens/Imgprofile.dart';
import 'package:forthapp/widgets/groupcard.dart';
import 'package:forthapp/widgets/userprofile.dart';
//to remve the line use elevete

class Homescreen extends StatelessWidget {
  const Homescreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        leading: IconButton(
            onPressed: () {
              print("ok");
              Userprofile();
            },
            icon: Icon(
              CupertinoIcons.search,
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
              )),
          GestureDetector(
              child: Padding(
                padding: EdgeInsets.fromLTRB(5, 7, 7, 5),
                child: imgprofile(
                  iamgeurl: currtenuser.iamgeurl,
                  size: 37,
                ),
              ),
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => Userprofile()));
              })
        ],
      ),
      body: Stack(
        alignment: Alignment.center,
        children: [
         ListView( 
          padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
          children: [
            ...grouplist.map((e) => Groupcard(group:e)),
            ...grouplist.map((e) => Groupcard(group:e)),
            ...grouplist.map((e) => Groupcard(group:e)),
            ...grouplist.map((e) => Groupcard(group:e)),
          ],
        ),
        Positioned(
          left: 0,
          right: 0,
          bottom: 0,
          child: Container(
            height: 80,
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end : Alignment.bottomCenter,
                colors: [
                  Theme.of(context).
                  scaffoldBackgroundColor.withOpacity(0.1),
                  Theme.of(context).scaffoldBackgroundColor,
                ]
                ),
            ),
          ),
          )
        ],
      ),
      

    );
  }
}
