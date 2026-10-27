"""Source-reference checks remain optional; runtime/distribution tests always run."""
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]


def pytest_collection_modifyitems(items):
    for item in items:
        name = item.originalname or item.name
        needs_source = (
            item.path.name == 'test_recovery.py'
            or (item.path.name == 'test_display_list.py' and 'document' in item.fixturenames)
            or name in ('test_registered_art_matches_original_timeline_and_embedded_bitmap',
                        'test_all_five_themes_have_complete_living_and_ruin_art',
                        'test_source_timeline_stop_scripts_execute_through_adapter'))
        if needs_source and not (ROOT / 'WorldDomination2.swf').exists():
            item.add_marker(pytest.mark.skip(reason='Optional source-verification fixtures are not distributed'))
        if name == 'test_initialized_menu_against_corresponding_original_ruffle_capture' and not (ROOT / 'validation/ruffle_menu').exists():
            item.add_marker(pytest.mark.skip(reason='Optional external-player reference captures are not distributed'))
