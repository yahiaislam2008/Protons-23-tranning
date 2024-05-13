import 'package:flutter/material.dart';
import 'package:forthapp/models/User.dart';

class Group {
  final String club;
  final String name;
  final List<User> speakers;
  final List<User> folbyspeakers;
  final List<User> others;

  Group({
    required this.club,
    required this.name,
    this.speakers = const[],
    this.folbyspeakers=const[],
    this.others=const[],
  });


     
}