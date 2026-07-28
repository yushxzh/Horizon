import json
from datetime import datetime, timezone
from pathlib import Path

from src.models import Config
from src.orchestrator import _summary_date


def load_github_config() -> Config:
    config_path = Path(__file__).parents[1] / "data" / "config.github.json"
    return Config.model_validate(json.loads(config_path.read_text(encoding="utf-8")))


def test_github_config_matches_personal_digest_contract() -> None:
    config = load_github_config()

    assert config.ai.provider.value == "deepseek"
    assert config.ai.api_key_env == "DEEPSEEK_API_KEY"
    assert config.ai.languages == ["zh"]
    assert config.filtering.time_window_hours == 24
    assert config.filtering.max_items == 20
    assert config.sources.hackernews.enabled is True
    assert len(config.sources.github) == 10
    assert len(config.sources.rss) == 10
    assert len(config.sources.reddit.subreddits) == 4
    assert config.sources.twitter is not None
    assert config.sources.twitter.mode == "apify"
    assert config.sources.twitter.apify_token_env == "APIFY_TOKEN"
    assert config.sources.twitter.actor_id == "automation-lab~twitter-scraper"
    assert config.sources.twitter.fetch_limit == 4
    assert config.sources.twitter.fetch_reply_text is False
    assert config.sources.telegram.enabled is False
    assert config.webhook is None


def test_summary_date_uses_shanghai_calendar_day() -> None:
    utc_evening = datetime(2026, 7, 28, 22, 35, tzinfo=timezone.utc)

    assert _summary_date(utc_evening) == "2026-07-29"
