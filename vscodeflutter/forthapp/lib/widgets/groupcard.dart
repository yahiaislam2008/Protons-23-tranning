import 'package:flutter/material.dart';
import 'package:forthapp/models/Group.dart';
import 'package:forthapp/scrrens/group.dart';

class Groupcard extends StatelessWidget {
  final Group group;
  const Groupcard({
    super.key,
    required this.group,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => Navigator.of(context).push(
        MaterialPageRoute(
          fullscreenDialog: true,
          builder: (_) => Groupscreen(group: group)
          ),
      ),
      child: Padding(
        padding: const EdgeInsets.only(top: 10),
        child: Card(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15)
          ),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                Text(
                  group.club.toUpperCase()
                ),
              ],
            ),),
        ),
      ),
    );
  }
}