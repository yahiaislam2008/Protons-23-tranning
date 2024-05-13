import "package:flutter/material.dart";

class User{
  final String firstname;
  final String lastname;
  final String country;
  final String iamgeurl; 
  const User({
    required this.firstname,
    required this.lastname,
    required this.country,
    required this.iamgeurl,
  }); 
}