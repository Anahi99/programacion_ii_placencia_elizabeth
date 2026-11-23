from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AutenticacionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('ana', 'ana@example.com', 'Clave-segura-123')

    def test_home_anonimo_redirige_al_login(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, f"{reverse('login')}?next={reverse('home')}")

    def test_login_correcto(self):
        resp = self.client.post(reverse('login'), {'username': 'ana', 'password': 'Clave-segura-123'})
        self.assertRedirects(resp, reverse('home'))

    def test_registro_crea_usuario_con_correo(self):
        resp = self.client.post(reverse('registro'), {
            'username': 'luis', 'email': 'luis@example.com',
            'password1': 'Otra-clave-456', 'password2': 'Otra-clave-456',
        })
        self.assertRedirects(resp, reverse('login'))
        self.assertEqual(User.objects.get(username='luis').email, 'luis@example.com')

    def test_registro_rechaza_correo_repetido(self):
        resp = self.client.post(reverse('registro'), {
            'username': 'otra', 'email': 'ana@example.com',
            'password1': 'Otra-clave-456', 'password2': 'Otra-clave-456',
        })
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(User.objects.filter(username='otra').exists())

    def test_logout_solo_por_post(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(reverse('logout')).status_code, 405)
        resp = self.client.post(reverse('logout'))
        self.assertRedirects(resp, reverse('login'))
        self.assertEqual(self.client.get(reverse('home')).status_code, 302)
