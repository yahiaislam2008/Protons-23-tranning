import 'package:flutter/material.dart';
import 'package:n5ames/model/friends.dart';
import 'package:n5ames/widgets/friendadd.dart';

class Friendcard extends StatelessWidget {
  final Friend friend ;
  const Friendcard({super.key, required this.friend});
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () { Navigator.of(context).push(
        MaterialPageRoute(
            fullscreenDialog: true, builder: (_) => friendadd(frien: friend)),
      );
      },
      child: Padding(
        padding: const EdgeInsets.only(top: 10),
        child: Card(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
          child: Padding(
            padding: const EdgeInsets.all(30),
            child: Column(
              children: [
                Text(friend.friendname.toUpperCase(),
                style: TextStyle(
                  fontSize: 30
                ),),
              ],
            ),
          ),
        ),
      ),
    );
  }
}