import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

const String baseUrl = 'http://10.0.2.2:5000/api'; // localhost no Android emulator
final storage = FlutterSecureStorage();

Future<bool> login(String username, String password) async {
  final response = await http.post(
    Uri.parse('$baseUrl/login'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'username': username, 'password': password}),
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    await storage.write(key: 'token', value: data['access_token']);
    return true;
  } else {
    return false;
  }
}

Future<List<dynamic>> getFundos() async {
  final token = await storage.read(key: 'token');

  final response = await http.get(
    Uri.parse('$baseUrl/fundos'),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token'
    },
  );

  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  } else {
    throw Exception('Erro ao carregar fundos');
  }
}

