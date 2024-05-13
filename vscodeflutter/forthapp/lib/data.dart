import 'package:forthapp/models/Group.dart';
import 'package:forthapp/models/User.dart';

const User currtenuser = User(
  firstname: "yahia",
  lastname: "islam",
  country: "Egypt",
  iamgeurl: 'https://static01.nyt.com/images/2022/04/04/multimedia/15ai-nocode/15ai-nocode-videoSixteenByNineJumbo1600.jpg');

const List<User> allusers =[
  User(
  firstname: "yahia",
  lastname: "islam",
  country: "Egypt",
  iamgeurl: 'https://static01.nyt.com/images/2022/04/04/multimedia/15ai-nocode/15ai-nocode-videoSixteenByNineJumbo1600.jpg'),
  User(
  firstname: "she2",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://static01.nyt.com/images/2022/04/04/multimedia/15ai-nocode/15ai-nocode-videoSixteenByNineJumbo1600.jpg'),

  User(
  firstname: "he3",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe'),
  User(
  firstname: "they4",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe'),
  User(
  firstname: "islam5",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe'),
  User(
  firstname: "yassen6",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe'),
  User(
  firstname: "daleen7",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe'),
  User(
  firstname: "dan8",
  lastname: "islam",
  country: "Egypt", 
  iamgeurl: 'https://bigmedia.bpifrance.fr/sites/default/files/styles/article_main_image/public/2022-01/shutterstock_332455154.jpg?itok=qiVcPKYe')
];

final List<Group> grouplist=[
  Group(
    club: "N5mes",
    name: "2ay name",
    speakers: (List<User>.from(allusers)..shuffle()).getRange(0, 3).toList(),
    folbyspeakers: List<User>.from(allusers)..shuffle(),
    others: List<User>.from(allusers)..shuffle(),
    ),
    Group(
    club: "revones",
    name: "zabt",
    speakers: (List<User>.from(allusers)..shuffle()).getRange(0, 3).toList(),
    folbyspeakers: List<User>.from(allusers)..shuffle(),
    others: List<User>.from(allusers)..shuffle(),
    ),
    Group(
    club: "g3an",
    name: "recipe",
    speakers: (List<User>.from(allusers)..shuffle()).getRange(0, 3).toList(),
    folbyspeakers: List<User>.from(allusers)..shuffle(),
    others: List<User>.from(allusers)..shuffle(),
    ),
    Group(
    club: "ana msh kadr",
    name: "lalc",
    speakers: (List<User>.from(allusers)..shuffle()).getRange(0, 3).toList(),
    folbyspeakers: List<User>.from(allusers)..shuffle(),
    others: List<User>.from(allusers)..shuffle(),
    )
];