🎯 Como integrar Django com Flutter
📦 Arquitetura
plaintext

Flutter App ↔️ REST API (Django + Django REST Framework)
O Flutter consome a API via http ou dio.

O Django REST Framework responde com JSON.

🔧 Etapas da Integração
✅ 1. Crie sua API com Django
Já tá com isso pronto, certo? Se não, você pode seguir esse exemplo de endpoint:

GET /api/funds/

json

[
  {
    "id": 1,
    "name": "Fundo Alpha",
    "ticker": "FALPHA",
    "type": "Renda Fixa",
    "quota_value": "100.50"
  }
]
✅ 2. Permitir acesso externo (CORS)
No settings.py do Django:

bash

pip install django-cors-headers
Adicione em INSTALLED_APPS e MIDDLEWARE:

python

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

# Permite acesso do Flutter
CORS_ALLOW_ALL_ORIGINS = True
# ou:
# CORS_ALLOWED_ORIGINS = ["http://localhost:PORT"]
✅ 3. No Flutter: fazer requisições HTTP
Use o pacote http ou dio:

bash

flutter pub add http
Exemplo com http:

dart

import 'package:http/http.dart' as http;
import 'dart:convert';

Future<List<dynamic>> fetchFunds() async {
  final response = await http.get(Uri.parse('http://10.0.2.2:8000/api/funds/'));

  if (response.statusCode == 200) {
    return json.decode(response.body);
  } else {
    throw Exception('Falha ao carregar fundos');
  }
}
⚠️ Use 10.0.2.2 em vez de localhost quando estiver usando o emulador Android.

✅ 4. Exibir dados no app Flutter
dart

FutureBuilder(
  future: fetchFunds(),
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      final funds = snapshot.data!;
      return ListView.builder(
        itemCount: funds.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(funds[index]['name']),
            subtitle: Text('Ticker: ${funds[index]['ticker']}'),
          );
        },
      );
    } else if (snapshot.hasError) {
      return Text('Erro: ${snapshot.error}');
    }
    return CircularProgressIndicator();
  },
)
✅ Requisitos no Flutter
Ter o Flutter SDK instalado

A API do Django rodando (localhost ou servidor remoto)

Configurar o IP corretamente (ex: 10.0.2.2 para Android Emulator)