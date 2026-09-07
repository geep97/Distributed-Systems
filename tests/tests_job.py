


def test_create_job(test_client):
    response = test_client.post(
        "/jobs",
        json={
            "job_type": "email",
            "payload": {
                "message": "Hello"
            }
        }
    )

    assert response.status_code == 200