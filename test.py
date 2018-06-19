
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="12dp"

        android:text="TextView"
        app:layout_constraintBottom_toTopOf="@+id/textView2"
        app:layout_constraintTop_toTopOf="parent"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp"
        android:text="TextView"
        app:layout_constraintBottom_toTopOf="@+id/textView3"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="20dp"
        android:text="TextView"
        app:layout_constraintBottom_toTopOf="@+id/textView4"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView4"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="4dp"
        android:text="TextView"
        app:layout_constraintBottom_toTopOf="@+id/textView5"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView5"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="TextView"
        tools:layout_editor_absoluteX="59dp"
        tools:layout_editor_absoluteY="116dp" />

    <TextView
        android:id="@+id/textView6"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:text="TextView"
        app:layout_constraintTop_toBottomOf="@+id/textView5"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView7"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="20dp"
        android:text="TextView"
        app:layout_constraintTop_toBottomOf="@+id/textView6"
        tools:layout_editor_absoluteX="59dp" />

    <TextView
        android:id="@+id/textView8"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="12dp"
        android:layout_marginTop="12dp"
        android:text="TextView"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView7"
        app:layout_constraintVertical_bias="0.0"
        tools:layout_editor_absoluteX="59dp" />
</android.support.constraint.ConstraintLayout>
