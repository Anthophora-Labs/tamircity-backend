# Generated by Django 4.1.7 on 2023-04-14 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0001_initial"),
        ("expertise_forms", "0002_expertisewatch"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExpertisePhone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("invoice", models.BooleanField(default=True)),
                ("box", models.BooleanField(default=True)),
                ("guarantee_term", models.IntegerField()),
                ("color", models.CharField(max_length=150)),
                ("imei_registration", models.CharField(max_length=150)),
                ("e_devlet_registration", models.CharField(max_length=150)),
                ("screen_size", models.CharField(max_length=150)),
                ("screen_technology", models.CharField(max_length=150)),
                ("screen_resolution", models.CharField(max_length=150)),
                ("scratch_resistance", models.BooleanField(default=True)),
                ("cpu_model", models.CharField(max_length=150)),
                ("cpu_frequency", models.IntegerField()),
                ("ram", models.IntegerField()),
                ("os_type", models.CharField(max_length=150)),
                ("os_type_version", models.CharField(max_length=150)),
                ("cpu_core_number", models.IntegerField()),
                ("camera_resolution", models.IntegerField()),
                ("front_camera_resolution", models.IntegerField()),
                ("video_record_resolution", models.CharField(max_length=150)),
                ("video_fps", models.IntegerField()),
                ("face_recognition", models.BooleanField(default=True)),
                ("slow_motion_video", models.BooleanField(default=True)),
                ("camera_ai", models.BooleanField(default=True)),
                ("timer", models.BooleanField(default=True)),
                ("automatic_focus", models.BooleanField(default=True)),
                ("geographic_location", models.BooleanField(default=True)),
                ("voice_control", models.BooleanField(default=True)),
                ("internal_storage", models.IntegerField()),
                ("external_storage", models.IntegerField()),
                ("max_external_storage", models.IntegerField()),
                ("battery_type", models.CharField(max_length=150)),
                ("battery_capacity", models.IntegerField()),
                ("battery_wireless_charge", models.BooleanField(default=True)),
                ("battery_fast_charge", models.BooleanField(default=True)),
                ("battery_wireless_fast_charge", models.BooleanField(default=True)),
                ("battery_detachable", models.BooleanField(default=True)),
                ("wifi_frequency", models.CharField(max_length=150)),
                ("nfc", models.BooleanField(default=True)),
                ("g5_support", models.BooleanField(default=True)),
                ("release_year", models.IntegerField()),
                ("resistance_of_water", models.BooleanField(default=True)),
                ("resistance_of_dust", models.BooleanField(default=True)),
                ("finger_print", models.BooleanField(default=True)),
                ("double_sim", models.BooleanField(default=True)),
                ("antutu_score", models.IntegerField()),
                ("is_screen_has_broken_problem", models.BooleanField(default=True)),
                (
                    "is_screen_has_obscuration_problem",
                    models.BooleanField(default=True),
                ),
                ("is_touch_screen_has_problem", models.BooleanField(default=True)),
                ("is_screen_has_dead_pixel", models.BooleanField(default=True)),
                ("is_device_has_case_problem", models.BooleanField(default=True)),
                ("is_device_has_cover_problem", models.BooleanField(default=True)),
                ("is_device_hav_e_cameras_problem", models.BooleanField(default=True)),
                ("is_device_hav_e_speaker_problem", models.BooleanField(default=True)),
                ("is_device_has_high_heat_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_charge_socket_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_power_button_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_opened_case_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_side_button_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_freezing_problem", models.BooleanField(default=True)),
                ("is_device_has_bluetooth_problem", models.BooleanField(default=True)),
                ("is_device_has_wifi_problem", models.BooleanField(default=True)),
                ("is_device_has_microphone_problem", models.BooleanField(default=True)),
                ("is_device_has_cellular_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_sound_transfer_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_expertise_phone",
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExpertisePc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("invoice", models.BooleanField(default=True)),
                ("box", models.BooleanField(default=True)),
                ("guarantee_term", models.IntegerField()),
                ("phone_color", models.CharField(max_length=150)),
                ("scren_size", models.DecimalField(decimal_places=2, max_digits=10)),
                ("screen_resolution", models.CharField(max_length=150)),
                ("screen_resolution_type", models.CharField(max_length=150)),
                ("screen_panel_type", models.CharField(max_length=150)),
                ("operating_system", models.CharField(max_length=150)),
                ("card_reader", models.BooleanField(default=True)),
                ("camera", models.BooleanField(default=True)),
                ("finger_print_reader", models.BooleanField(default=True)),
                ("touch_screen", models.BooleanField(default=True)),
                ("keyboard_backlight", models.BooleanField(default=True)),
                ("cpu", models.CharField(max_length=150)),
                ("cpu_serie", models.CharField(max_length=150)),
                (
                    "cpu_base_frequency",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("cpu_core_number", models.IntegerField()),
                ("cpu_ram", models.IntegerField()),
                ("intel_turbo_boost", models.BooleanField(default=True)),
                ("ram", models.IntegerField()),
                ("ram_frequency", models.CharField(max_length=150)),
                ("ram_type", models.CharField(max_length=150)),
                ("hdd_capacity", models.IntegerField()),
                ("ssd", models.BooleanField(default=True)),
                ("ssd_capacity", models.IntegerField()),
                ("external_graphics_card", models.BooleanField(default=True)),
                ("external_graphics_card_brand", models.CharField(max_length=150)),
                ("external_graphics_card_series", models.CharField(max_length=150)),
                ("external_graphics_card_memory", models.CharField(max_length=150)),
                ("external_graphics_card_bit", models.IntegerField()),
                ("external_graphics_card_core_speed", models.IntegerField()),
                ("internal_graphic_card_cpu", models.CharField(max_length=150)),
                ("graphic_base_frequency", models.IntegerField()),
                ("graphic_max_dynamic_frequency", models.IntegerField()),
                ("four_k", models.BooleanField(default=True)),
                ("direct_x", models.BooleanField(default=True)),
                ("open_gl", models.DecimalField(decimal_places=2, max_digits=10)),
                ("supperted_screen_number", models.IntegerField()),
                ("ethernet", models.BooleanField(default=True)),
                ("ethernet_version", models.BooleanField(default=True)),
                ("wifi_version", models.CharField(max_length=150)),
                ("hdmi", models.BooleanField(default=True)),
                ("bluetooth", models.BooleanField(default=True)),
                ("usb_2_number", models.IntegerField()),
                ("usb_3_number", models.IntegerField()),
                ("usb_type_c_number", models.IntegerField()),
                ("is_screen_has_broken_problem", models.BooleanField(default=True)),
                ("is_screen_has_loss_problem", models.BooleanField(default=True)),
                ("is_screen_has_dead_pixel", models.BooleanField(default=True)),
                ("is_device_has_case_problem", models.BooleanField(default=True)),
                ("is_device_has_cover_problem", models.BooleanField(default=True)),
                (
                    "is_keyboard_has_broken_key_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_keyboard_has_function_less_key_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_charge_socket_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_touch_pad_problem", models.BooleanField(default=True)),
                ("is_device_has_speaker_problem", models.BooleanField(default=True)),
                ("is_device_has_high_heat_problem", models.BooleanField(default=True)),
                ("is_device_has_high_sound_problem", models.BooleanField(default=True)),
                ("is_device_has_dvd_driver_problem", models.BooleanField(default=True)),
                ("is_device_has_usb_input_problem", models.BooleanField(default=True)),
                ("is_device_has_usb_type_c_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_card_reader_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_camera_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_finger_print_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_mother_board_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_ram_problem", models.BooleanField(default=True)),
                ("is_device_has_hdd_problem", models.BooleanField(default=True)),
                ("is_device_has_ssd_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_external_graphic_card_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_internal_graphic_card_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_optical_reader_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_ethernet_connection_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_wifi_problem", models.BooleanField(default=True)),
                ("is_device_has_hdmi_problem", models.BooleanField(default=True)),
                ("is_device_has_bluetooth_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_head_phone_socket_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_touch_screen_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_keyboard_backlight_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_expertise_pc",
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExpertiseConsole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("invoice", models.BooleanField(default=True)),
                ("box", models.BooleanField(default=True)),
                ("guarantee_term", models.IntegerField()),
                ("color", models.CharField(max_length=150)),
                ("platform", models.CharField(max_length=150)),
                ("storage_capacity", models.IntegerField()),
                ("os_type", models.CharField(max_length=150)),
                ("cpu_model", models.CharField(max_length=150)),
                ("fps_value", models.IntegerField()),
                ("hdr_support", models.BooleanField(default=True)),
                ("ram", models.IntegerField()),
                ("ram_type", models.CharField(max_length=150)),
                ("game_resolution", models.CharField(max_length=150)),
                ("video_resolution", models.CharField(max_length=150)),
                ("network_type", models.CharField(max_length=150)),
                ("ethernet", models.BooleanField(default=True)),
                ("ethernet_speed", models.IntegerField()),
                ("hdmi_standard", models.CharField(max_length=150)),
                ("usb_input", models.IntegerField()),
                ("usb_inputNumber", models.IntegerField()),
                ("usb_version", models.CharField(max_length=150)),
                ("bluetooth", models.BooleanField(default=True)),
                ("bluetooth_version", models.CharField(max_length=150)),
                ("voice_support", models.BooleanField(default=True)),
                ("controller", models.BooleanField(default=True)),
                ("controller_number", models.IntegerField()),
                ("game", models.BooleanField(default=True)),
                ("game_number", models.IntegerField()),
                ("is_box_has_problem", models.BooleanField(default=True)),
                ("is_box_has_light_problem", models.BooleanField(default=True)),
                ("is_controller_has_light_problem", models.BooleanField(default=True)),
                (
                    "is_controller_has_vibration_problem",
                    models.BooleanField(default=True),
                ),
                ("is_controller_Has_analog_problem", models.BooleanField(default=True)),
                ("is_controller_HasButtonProblem", models.BooleanField(default=True)),
                ("is_device_has_button_problem", models.BooleanField(default=True)),
                ("is_device_has_usb_problem", models.BooleanField(default=True)),
                ("is_controller_has_usb_problem", models.BooleanField(default=True)),
                ("is_device_has_heat_problem", models.BooleanField(default=True)),
                ("is_device_has_high_sound_problem", models.BooleanField(default=True)),
                (
                    "is_device_has_network_connection_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_optical_driver_problem",
                    models.BooleanField(default=True),
                ),
                (
                    "is_device_has_disk_reading_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_ethernet_problem", models.BooleanField(default=True)),
                ("is_device_has_hdmi_problem", models.BooleanField(default=True)),
                (
                    "is_device_have_usb_inputs_problem",
                    models.BooleanField(default=True),
                ),
                ("is_device_has_bluetooth_problem", models.BooleanField(default=True)),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_expertise_console",
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
    ]